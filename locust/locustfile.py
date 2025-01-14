import os
from locust import FastHttpUser, task, between

TOKEN = os.environ["AZURE_ENTRA_TOKEN"]
AUTH = {"Authorization": f"Bearer {TOKEN}"}


class BrpUpdate(FastHttpUser):
    wait_time = between(5, 15)

    @task(2)
    def get_volgindicatie(self):
        bsn = 555555026
        with self.rest(
            "GET",
            f"/haalcentraal/api/brpupdate/volgindicaties/{bsn}",
            headers=AUTH,
        ) as resp:
            if resp.js is None:
                pass  # no need to do anything, already marked as failed
            elif "burgerservicenummer" not in resp.js:
                resp.failure(f"'burgerservicenummer' missing from response {resp.text}")
            elif resp.js["burgerservicenummer"] != bsn:
                resp.failure(
                    f"'burgerservicenummer' had an unexpected value: {resp.js['burgerservicenummer']}"
                )

    @task(3)
    def get_volgindicaties(self):
        with self.rest(
            "GET",
            "/haalcentraal/api/brpupdate/volgindicaties",
            headers=AUTH,
        ) as resp:
            if resp.js is None:
                pass  # no need to do anything, already marked as failed
            elif "volgindicaties" not in resp.js:
                resp.failure(f"'volgindicaties' missing from response {resp.text}")
            elif "burgerservicenummer" not in resp.js["volgindicaties"][0]:
                resp.failure(f"'burgerservicenummer' missing from response {resp.text}")

    @task(5)
    def get_gewijzigde_personen(self):
        with self.rest(
            "GET",
            "/haalcentraal/api/brpupdate/wijzigingen?vanaf=2024-10-01",
            headers=AUTH,
        ) as resp:
            if resp.js is None:
                pass  # no need to do anything, already marked as failed
            elif "burgerservicenummers" not in resp.js:
                resp.failure(
                    f"'burgerservicenummers' missing from response {resp.text}"
                )

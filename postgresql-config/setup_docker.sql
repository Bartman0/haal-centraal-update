--
-- PostgreSQL database dump
--

-- Dumped from database version 15.8 (Homebrew)
-- Dumped by pg_dump version 16.4

-- Started on 2024-11-02 20:42:57 CET

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_table_access_method = heap;

--
-- TOC entry 225 (class 1259 OID 25019)
-- Name: bsn_lijst; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.bsn_lijst (
    burgerservicenummer bigint NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


--
-- TOC entry 224 (class 1259 OID 25012)
-- Name: volgindicaties; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.volgindicaties (
    afnemer_code text NOT NULL,
    burgerservicenummer bigint NOT NULL,
    begindatum date NOT NULL,
    einddatum date NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


--
-- TOC entry 3621 (class 0 OID 25019)
-- Dependencies: 225
-- Data for Name: bsn_lijst; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.bsn_lijst (burgerservicenummer, updated_at) FROM stdin;
555555021	2024-11-01 23:01:28.590918
555555025	2024-11-01 23:01:46.005419
\.


--
-- TOC entry 3620 (class 0 OID 25012)
-- Dependencies: 224
-- Data for Name: volgindicaties; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.volgindicaties (afnemer_code, burgerservicenummer, begindatum, einddatum, updated_at) FROM stdin;
test	555555025	2024-10-29	2025-01-23	2024-10-29 18:34:56.018044
afnemer_test	555555021	2024-11-01	2025-01-23	2024-11-01 00:58:25.749458
afnemer_test	555555025	2024-11-01	2025-01-23	2024-11-01 23:28:57.199557
afnemer_test	555555026	2024-11-02	2025-01-23	2024-11-02 00:25:21.171485
\.


--
-- TOC entry 3477 (class 2606 OID 25023)
-- Name: bsn_lijst bsn_lijst_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.bsn_lijst
    ADD CONSTRAINT bsn_lijst_pkey PRIMARY KEY (burgerservicenummer);


--
-- TOC entry 3475 (class 2606 OID 25018)
-- Name: volgindicaties volgindicaties_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.volgindicaties
    ADD CONSTRAINT volgindicaties_pkey PRIMARY KEY (afnemer_code, burgerservicenummer, begindatum);


-- Completed on 2024-11-02 20:43:00 CET

--
-- PostgreSQL database dump complete
--


-- Table: public.volgindicaties

--DROP TABLE IF EXISTS public.volgindicaties;

CREATE TABLE IF NOT EXISTS public.volgindicaties
(
    afnemer_code text COLLATE pg_catalog."default" NOT NULL,
    burgerservicenummer bigint NOT NULL,
    begindatum date NOT NULL,
    einddatum date NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    CONSTRAINT volgindicaties_pkey PRIMARY KEY (afnemer_code, burgerservicenummer, begindatum)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.volgindicaties
    OWNER to richardkooijman;


-- Table: public.bsn_lijst

--DROP TABLE IF EXISTS public.bsn_lijst;

CREATE TABLE IF NOT EXISTS public.bsn_lijst
(
    burgerservicenummer bigint NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    CONSTRAINT bsn_lijst_pkey PRIMARY KEY (burgerservicenummer)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.bsn_lijst
    OWNER to richardkooijman;

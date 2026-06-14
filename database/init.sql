CREATE TABLE IF NOT EXISTS tenants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(120) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    tenant_id INTEGER REFERENCES tenants(id),
    name VARCHAR(255) DEFAULT '',
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role VARCHAR(50) DEFAULT 'sales',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS companies (
    id SERIAL PRIMARY KEY,
    tenant_id INTEGER REFERENCES tenants(id),
    company_name VARCHAR(255) NOT NULL,
    website VARCHAR(255) DEFAULT '',
    country VARCHAR(120) DEFAULT '',
    industry VARCHAR(120) DEFAULT '',
    source VARCHAR(120) DEFAULT '',
    status VARCHAR(80) DEFAULT 'NEW',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    tenant_id INTEGER REFERENCES tenants(id),
    company_id INTEGER REFERENCES companies(id),
    first_name VARCHAR(120) DEFAULT '',
    last_name VARCHAR(120) DEFAULT '',
    job_title VARCHAR(255) DEFAULT '',
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(120) DEFAULT '',
    whatsapp VARCHAR(120) DEFAULT '',
    linkedin VARCHAR(255) DEFAULT '',
    owner_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS leads (
    id SERIAL PRIMARY KEY,
    tenant_id INTEGER REFERENCES tenants(id),
    company_id INTEGER REFERENCES companies(id),
    contact_id INTEGER REFERENCES contacts(id),
    owner_id INTEGER REFERENCES users(id),
    source VARCHAR(120) DEFAULT 'MANUAL',
    status VARCHAR(80) DEFAULT 'NEW',
    level VARCHAR(20) DEFAULT 'C',
    score INTEGER DEFAULT 0,
    probability INTEGER DEFAULT 0,
    expected_amount NUMERIC(12,2) DEFAULT 0,
    next_followup DATE,
    note TEXT DEFAULT '',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS emails (
    id SERIAL PRIMARY KEY,
    tenant_id INTEGER REFERENCES tenants(id),
    company_id INTEGER REFERENCES companies(id),
    contact_id INTEGER REFERENCES contacts(id),
    direction VARCHAR(20) NOT NULL,
    subject TEXT DEFAULT '',
    body TEXT DEFAULT '',
    from_email VARCHAR(255) DEFAULT '',
    to_email TEXT DEFAULT '',
    message_id VARCHAR(255) UNIQUE,
    thread_id VARCHAR(255) DEFAULT '',
    received_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS timeline (
    id SERIAL PRIMARY KEY,
    tenant_id INTEGER REFERENCES tenants(id),
    company_id INTEGER REFERENCES companies(id),
    contact_id INTEGER REFERENCES contacts(id),
    lead_id INTEGER REFERENCES leads(id),
    event_type VARCHAR(120) NOT NULL,
    event_data JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    tenant_id INTEGER REFERENCES tenants(id),
    company_id INTEGER REFERENCES companies(id),
    contact_id INTEGER REFERENCES contacts(id),
    lead_id INTEGER REFERENCES leads(id),
    owner_id INTEGER REFERENCES users(id),
    title VARCHAR(255) NOT NULL,
    description TEXT DEFAULT '',
    due_date DATE,
    status VARCHAR(50) DEFAULT 'TODO',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO tenants (name, slug)
VALUES ('SOGRACE', 'sograce')
ON CONFLICT (slug) DO NOTHING;

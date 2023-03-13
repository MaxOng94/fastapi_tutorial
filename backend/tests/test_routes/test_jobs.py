def test_create_jobs(client):
    data = {
        "title": "Prompt Engineer",
        "company": "Google",
        "company_url": "www.google.com",
        "location": "metaverse",
        "description": "eat poop",
        "date_posted": "2023-04-01",
        "owner_id": 5,
    }
    # use json=data
    response = client.post("/jobs/create-job/", json=data)
    assert response.status_code == 200
    assert response.json()["location"] == "metaverse"
    assert response.json()["description"] == "eat poop"


def test_read_job(client):  # new test
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
        "owner_id": 2,
    }
    response = client.post("/jobs/create-job/", json=data)
    job_id = response.json()["id"]
    response = client.get(f"/jobs/get-jobs/{job_id}/")
    print(response)
    assert response.status_code == 200
    assert response.json()["title"] == "SDE super"


def test_read_all_jobs(client):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    client.post("/jobs/create-job/", json=data)
    client.post("/jobs/create-job/", json=data)

    response = client.get("/jobs/all-jobs/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


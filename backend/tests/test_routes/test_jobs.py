from fastapi import status

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


def test_delete_job(client):  # new test
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
    user_id = data["owner_id"]
    msg = client.delete(f"/jobs/delete/{user_id}/{job_id}")
    response = client.get(f"/jobs/get-jobs/{job_id}/")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_update_job(client):  # new test
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
    user_id = data["owner_id"]
    data['title'] ="new job post title"
    response = client.put(f"/jobs/update/{user_id}/{job_id}", json=data)
    assert response.status_code == 200
    assert response.json()["title"] == "new job post title"
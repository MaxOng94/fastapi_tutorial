import json


def test_create_jobs(client):
    data = {"title":"Prompt Engineer","company":"Google","company_url":"www.google.com",
            "location" :"metaverse",
            "description" : "eat poop",
            "date_posted" :"2023-04-01",
            "owner_id": 5
            }
    # use json=data 
    response = client.post("/jobs/",json= data)
    assert response.status_code == 200 
    assert response.json()["location"] == "metaverse"
    assert response.json()["description"] == "eat poop"
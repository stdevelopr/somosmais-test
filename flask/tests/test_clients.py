from app import df

def test_clients(client):
    """ Test the clients view response and pagination"""
    resp = client.get("/clients/")
    assert resp.status_code == 200
    assert resp.content_type == "application/json"
    assert "totalCount" and "pageSize" and "pageNumber" and "users" in resp.json
    assert len(resp.json['users']) == len(df)


def test_clients_paginate(client):
    """ Assert that the pagination returns the correct number of users """
    resp = client.get("/clients/", query_string={'pageSize': 5, 'pageNumber': 1})
    if len(df) > 5:
        assert len(resp.json['users']) == 5

def test_clients_filter(client):
    """ Assert that all clients satisfy the filter parameters """
    resp = client.get("/clients/", query_string={'region': 'norte', 'type': 'laborious'})
    for c in resp.json['users']:
        assert c['location']['region'] == 'norte'
        assert c['type'] == 'laborious'


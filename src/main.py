from fastapi import FastAPI

app = FastAPI(
    title="UMS",
    summary="User Management System",
    description="This is a User Management System API built using FastAPI. It provides endpoints for managing user data, including creating, retrieving, updating, and deleting user records.",
    version="1.0.0",
    contact={
        "name": "Vissu",
        "email": "viswanadh.adapala.25@outlook.com"
    },
    license_info={

    }
)
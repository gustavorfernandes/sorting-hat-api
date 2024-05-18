import uvicorn


if __name__ == "__main__":
    uvicorn.run("interface_adapters.api:app", host="0.0.0.0", port=8000)

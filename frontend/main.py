# type: ignore[attr-defined]
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from models.contract import Contract
from use_cases.contract import list_contracts
from requests.models.contract import build_list_contracts_request
from repository.repo import Repository


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

repo = Repository()


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/contracts", response_class=HTMLResponse)
def list_contracts_endpoint(request: Request):
    sysreq = build_list_contracts_request()
    sysresp = list_contracts(repo, sysreq)

    if sysresp:
        context = {"request": request, "contracts": sysresp.value}
        return templates.TemplateResponse("list_contracts.html", context)

    raise HTTPException(status_code=sysresp.status_code, detail=sysresp.value)

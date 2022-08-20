# type: ignore[attr-defined]
from datetime import date
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from use_cases.contract import list_contracts, create_contract
from use_cases.school import list_schools
from requests.models.contract import (
    build_list_contracts_request,
    build_create_contract_request,
)
from requests.models.school import build_list_schools_request
from repository.repo import Repository


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

repo = Repository()


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/contratos", response_class=HTMLResponse)
def list_contracts_endpoint(request: Request):
    sysreq = build_list_contracts_request()  # TODO: Pass filters
    sysresp = list_contracts(repo, sysreq)

    if sysresp:
        context = {"request": request, "contracts": sysresp.value}
        return templates.TemplateResponse("list_contracts.html", context)

    raise HTTPException(status_code=sysresp.status_code, detail=sysresp.value)


@app.get("/contratos/criar", response_class=HTMLResponse)
def create_contract_endpoint(request: Request):
    sysreq = build_list_schools_request()  # TODO: Pass filters
    sysresp = list_schools(repo, sysreq)

    if sysresp:
        context = {"request": request, "schools": sysresp.value}
        return templates.TemplateResponse("create_contract.html", context)

    raise HTTPException(status_code=sysresp.status_code, detail=sysresp.value)


@app.post("/contratos/enviar", response_class=RedirectResponse)
def post_contract(
    request: Request,
    school_id: int = Form(...),
    mat: str = Form(...),
    start: date = Form(...),
    end: date = Form(...),
    work_hours: int = Form(...),
):
    sysreq = build_create_contract_request(school_id, mat, start, end, work_hours)
    sysresp = create_contract(repo, sysreq)

    if sysresp:
        return RedirectResponse(url="/contratos", status_code=303)

    raise HTTPException(status_code=sysresp.status_code, detail=sysresp.value)

FROM python:3.11

# set working directory
RUN mkdir "backend"
WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# install dependencies
COPY app/requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt && pip install gunicorn

# add app
COPY .. .

# run project
#CMD alembic revision --autogenerate -m "Initial tables"  \
#    && alembic upgrade head \
#    && uvicorn app.main:app --host 0.0.0.0 --port 8000

CMD python rewrite_db_info.py \
    && gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000

#ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
#["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]
#ENTRYPOINT ["bash"]

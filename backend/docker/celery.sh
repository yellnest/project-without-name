#!/bin/bash

celery --app=app.tasks.celery_app:celery_app worker -l INFO

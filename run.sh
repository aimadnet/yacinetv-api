#!/usr/bin/env bash

set -e
set -x

uvicorn app:app --reload
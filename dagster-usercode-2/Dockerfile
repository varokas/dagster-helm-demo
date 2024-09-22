# https://github.com/dagster-io/dagster/blob/58b76cc1774e4144c1f88b25ed2d59ae7e81b87d/python_modules/automation/automation/docker/images/user-code-example/Dockerfile
FROM python:3.9-slim
# To make sure ubuntu does not ask for timezone region interactively
ENV DEBIAN_FRONTEND=noninteractive 
WORKDIR /opt/workspace
RUN pip install uv
COPY pyproject.toml uv.lock /opt/workspace/
RUN uv export --frozen --format requirements-txt -o requirements.txt
RUN uv pip install --system -r requirements.txt

COPY . /opt/workspace
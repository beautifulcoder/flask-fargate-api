#!/usr/bin/env python3
import aws_cdk as cdk

from flask_fargate_api.flask_fargate_api_stack import FlaskFargateApiStack


app = cdk.App()
FlaskFargateApiStack(
    app,
    "flask-fargate-api-stack",
    env=cdk.Environment(account='1234567890', region='us-east-1')
)

app.synth()

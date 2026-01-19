#!/usr/bin/env python3
import aws_cdk as cdk
from stacks.lab_serverless_stack import LabServerlessStack

app = cdk.App()
LabServerlessStack(app, "LabServerlessStack")
app.synth()
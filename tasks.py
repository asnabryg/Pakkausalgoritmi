from invoke import task
from invoke.tasks import Task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@Task
def test(ctx):
    ctx.run("pytest src")
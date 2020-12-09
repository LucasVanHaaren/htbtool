import click
from os import path, listdir

COMMAND_FOLDER = path.join(path.dirname(__file__), "commands")


class CLI(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        for filename in listdir(COMMAND_FOLDER):
            if filename.endswith(".py"):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = path.join(COMMAND_FOLDER, name + ".py")
        try:
            f = open(fn)
        except FileNotFoundError:
            return None
        else:
            code = compile(f.read(), fn, "exec")
            eval(code, ns, ns)
            return ns["command"]


@click.group(
    cls=CLI, help="CLI tool to manage pentest-related data on the hackthebox platform."
)
@click.pass_context
@click.option("--verbose", is_flag=True, help="Show extended information.")
def main(context, verbose):
    pass


if __name__ == "__main__":
    main()

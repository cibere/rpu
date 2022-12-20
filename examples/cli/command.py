from rpu.cli import ConsoleClient

# creating our client instance.
# It also accepts a `help_command` argument, though it is optional
# and we will use the default help_command for this example
client = ConsoleClient()


# using the decorator `client.command`
# will make it so we don't have to manually add the command and monkey patch a callback
# in the decorator we can set the name, description, brief (short description) and aliases
# if we do not set a name, it will take the functions name. In this case: 'test_cmd'
# if we do not pass a description, it will use the functions docstring. Though sice we do not add a docstring, it will not have a description
@client.command(
    name="test-cmd",
    description="the commands long description",
    brief="short cmd description",
    aliases=["test-cmd-aliase"],
)
def test_cmd():
    print("Hello from test command!")


# starting the client
client.run()

# Errors i get when trying to execute "flask db seed"

(venv) chris@DESKTOP-QRQO39E:~/online_library$ flask db seed
Traceback (most recent call last):
  File "/home/chris/online_library/venv/bin/flask", line 8, in <module>
    sys.exit(main())
  File "/home/chris/online_library/venv/local/lib/python2.7/site-packages/flask/cli.py", line 967, in main
    cli.main(args=sys.argv[1:], prog_name="python -m flask" if as_module else None)
  File "/home/chris/online_library/venv/local/lib/python2.7/site-packages/flask/cli.py", line 586, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/home/chris/online_library/venv/local/lib/python2.7/site-packages/click/core.py", line 782, in main
    rv = self.invoke(ctx)
  File "/home/chris/online_library/venv/local/lib/python2.7/site-packages/click/core.py", line 1254, in invoke
    cmd_name, cmd, args = self.resolve_command(ctx, args)
  File "/home/chris/online_library/venv/local/lib/python2.7/site-packages/click/core.py", line 1297, in resolve_command
    cmd = self.get_command(ctx, cmd_name)
  File "/home/chris/online_library/venv/local/lib/python2.7/site-packages/flask/cli.py", line 542, in get_command
    rv = info.load_app().cli.get_command(ctx, name)
  File "/home/chris/online_library/venv/local/lib/python2.7/site-packages/flask/cli.py", line 388, in load_app
    app = locate_app(self, import_name, name)
  File "/home/chris/online_library/venv/local/lib/python2.7/site-packages/flask/cli.py", line 259, in locate_app
    return find_app_by_string(script_info, module, app_name)
  File "/home/chris/online_library/venv/local/lib/python2.7/site-packages/flask/cli.py", line 184, in find_app_by_string
    app = call_factory(script_info, attr, args)
  File "/home/chris/online_library/venv/local/lib/python2.7/site-packages/flask/cli.py", line 119, in call_factory
    return app_factory()
  File "/home/chris/online_library/main.py", line 14, in create_app
    from commands import db_commands
  File "/home/chris/online_library/commands.py", line 3, in <module>
    from  models.authors import Author
ImportError: No module named models.authors


3 2/3 of my cli commands work fine, seed command does not work

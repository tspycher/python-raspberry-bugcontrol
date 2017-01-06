import argparse
import logging
import sys

def main():

    # CLI arguments
    parser = argparse.ArgumentParser(description='Staring Flask based RESTful Server')
    parser.add_argument('port', metavar='Port', type=int, nargs='?', default=5000, help='port to run the application')
    parser.add_argument('--interactive', '-i', dest='interactive', action='store_true', help='only run interactive frontend')
    args = parser.parse_args()

    if args.interactive:
        from pythonraspberrybugcontrol.lib import Bug
        bug = Bug()
        bug.bringToLife(interactive=True)
        sys.exit(0)

    from pythonraspberrybugcontrol import create_app
    from logging import StreamHandler

    (app, bug) = create_app()

    handler = StreamHandler()
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)

    app.logger.warning("running")
    bug.setLogger(app.logger)
    bug.bringToLife(interactive=False)
    app.run(host='0.0.0.0', port=args.port)

if __name__ == "__main__":
    main()
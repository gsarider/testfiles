#
# master template for python software
#
# variable and module naming snake_case
#
# -*- coding: utf-8 -*-




# imports
# variables
# functions



def run_loop(interval):
    """
    Run as main part loop and sleep specified interval
    """

    while True:
        logger.debug("Starting Update")
        logger.debug("continuing update")
        
        main()

        logger.debug("sleeping %s...", interval)

        sleep(interval)
 		return None
 
 
 def main ()
     """main loop"""
# do the work
 
 
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="geny")

    parser.add_argument(
        "-V",
        "--version",
        help="Print version and exit",
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "-v",
        "--verbose",
        help="Emit Verbose message stream",
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "-D", "--debug", help="Emit Debug messages", action="store_true", default=False
    )

    parser.add_argument(
        "-d", "--daemon", help="Run as a daemon", action="store_true", default=False
    )

    parser.add_argument(
        "-o", "--once", help="Run once and exit", action="store_true", default=False
    )

    parser.add_argument(
        "-l", "--log", help="File for logging", action="store", default=None
    )

    parser.add_argument(
        "-i",
        "--interval",
        help="Interval between cycles in seconds",
        action="store",
        type=int,
        default=60,
    )

    parser.add_argument(
        "-s",
        "--server",
        help="dump1090 server hostname (default localhost)",
        nargs=1,
        action="store",
        default=None,
    )

    parser.add_argument(
        "-p",
        "--port",
        help="alt-http port on dump1090 server (default 8080)",
        action="store",
        type=int,
        default=None,
    )

    args = parser.parse_args()

    if args.version:
        print(f"{parser.prog} version: {GENY_VERSION}")
        sys.exit()

    if args.verbose:
        logger.setLevel(logging.INFO)

    if args.debug:
        logger.setLevel(logging.DEBUG)

    if args.log:
        # opens a second logging instance specifically for logging
        logger.debug("Adding FileHandler to logger with filename %s", args.log)
        cl = logging.FileHandler(args.log)
        logger.addHandler(cl)
        cl.setLevel(logging.INFO)

    if args.daemon:
        with daemon.DaemonContext():
            run_loop(args.interval)
    else:
        try:
            logger.debug("Starting main processing loop")
            run_loop(args.interval)

        except KeyboardInterrupt:
            logger.warning("Received Keyboard Interrupt -- Exiting...")
            sys.exit()

    # use something like this for the K4 ip addr/port
    if args.server:
        K4_IP = args.server
    elif config.SERVER:
        K4_IP = config.SERVER
    else:
        K4_IP = "192.168.147.20"
        print(K4_IP)

    if args.port:
        port = args.port
    elif config.PORT:
        port = config.PORT
    else:
        port = 8080

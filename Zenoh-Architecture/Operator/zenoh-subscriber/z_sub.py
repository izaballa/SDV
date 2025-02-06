import time
import zenoh


def main(conf: zenoh.Config, key: str):
    # Initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:

        print(f"Declaring Subscriber on '{key}'...")

        def listener(sample: zenoh.Sample):
            print(
                f">> [Subscriber] Received {sample.kind} ('{sample.key_expr}': '{sample.payload.to_string()}')"
            )

        session.declare_subscriber(key, listener)

        print("Press CTRL-C to quit...")
        while True:
            time.sleep(1)


# Command line argument parsing
if __name__ == "__main__":
    import argparse
    import json
    import common

    parser = argparse.ArgumentParser(prog="z_sub", description="zenoh sub example")
    common.add_config_arguments(parser)
    parser.add_argument(
        "--key",
        "-k",
        dest="key",
        default="vehicle/1/**", # Modify
        type=str,
        help="The key expression to subscribe to.",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.key)

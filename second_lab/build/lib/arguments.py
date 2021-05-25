import argparse
import configparser


def get_files():
    parser = argparse.ArgumentParser(description='Great Description To Be Here')
    parser.add_argument(
        "-f",
        "--first_par",
        help="display a file will be  parsed"
        )
    parser.add_argument(
        "-s",
        "--second_par",
        help="display extension parse into"
        )
    parser.add_argument(
        "-c",
        "--config",
        help="configuration file")

    args = parser.parse_args()

    if args.config:
        return config_work(args.config)
    else:
        return(
            {
                args.first_par:args.first_par.split('.')[1],
                "extension":args.second_par
                }
        )
    
def config_work(file):
    config = configparser.ConfigParser()
    config.read(file)
    return (
        {
            config['FILE']['name']:config['FILE']['name'].split('.')[1],
            "extension":config['FORMAT']['extension']
            }
    )



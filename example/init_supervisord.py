import share_data


def main(*args):
    logger_obj = args[0]
    logger_obj.info("============================ in init_supervisord")
    print("init_supervisor.py:", share_data.dict_data[1])
    pass


if __name__ == "__main__":
    main()

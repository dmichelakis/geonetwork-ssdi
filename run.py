from helpers.process import Pre


def main():

    pre_process = Pre()
    data = pre_process.transform_response_body_to_a_python_data_structure_for_further_processing('/me')
    print(data)


if __name__ == "__main__":
    main()

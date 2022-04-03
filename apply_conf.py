import os
import toml

if __name__ == "__main__":

    file_path = os.path.dirname(os.path.realpath(__file__)) + "/conf.toml"
    try:
        parsed = toml.load(file_path)
    except:
        print("Error conf file not found.")
    # end try

    for service in parsed:
        try:
            conf_file = parsed[service]["conf_file"]
        except:
            print(f"configuration file for {service}, not found. Continuing.")
            continue
        # end try

        for root, dirs, files in os.walk(os.curdir):
            if conf_file in files:

                with open(root + "/" + conf_file, "r") as tmpl_file:
                    data = tmpl_file.read()
                # end with

                for conf_vars in parsed[service]:
                    data = data.replace(
                        f"<{conf_vars}>", parsed[service][conf_vars])
                # end for

                with open(root + "/" + conf_file.replace(".tmpl", ""), 'w') as file:
                    file.write(data)
                # end with
            # end if
        # end for
    # end for
# end main

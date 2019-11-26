import urlproc
import fileproc

base_path = os.getenv("BASE_PATH", "")
file_types = os.getenv("FILE_TYPES", "").split(",")
print_all = os.getenv("PRINT_ALL", "")

# get all file paths
file_paths = fileproc.get_file_paths(base_path, file_types)

# loop files
for file in file_paths:

    # collect links from each file
    urls = fileproc.collect_links_from_file(file)

    # if some links are found, check them
    if urls != []:
        print("\n", file, "\n", "-" * len(file))
        urlproc.check_urls(file, urls)

    # if no urls are found, mention it if required
    else:
        if print_all == True:
            print("\n", file, "\n", "-" * len(file))
            print("No urls found.")
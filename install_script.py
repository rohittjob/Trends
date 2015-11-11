import pip


def install(package):
    # Debugging
    # pip.main(["install", "--pre", "--upgrade", "--no-index",
    #         "--find-links=.", package, "--log-file", "log.txt", "-vv"])
    pip.main(["install", "--upgrade", "--no-index", "--find-links=.\\wheelhouse", package])


if __name__ == "__main__":
    install("psutil")
    raw_input("Press Enter to Exit...\n")

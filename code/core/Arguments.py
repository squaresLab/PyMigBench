import argparse


class Arguments:
    def __init__(self, query: str,
                 data_types: list[str] = [],
                 filters: list[str] = []):
        self.query = query
        self.data_types = data_types
        self.filters = parse_filters(filters)

    def __str__(self):
        return str(self.__dict__)


def parse_filters(filter_list: list[str]):
    if not filter_list:
        return {}
    dict = {}
    for filter in filter_list:
        attr, value = filter.split("=")
        dict[attr] = value

    return dict


def build_arguments() -> Arguments:
    parser = argparse.ArgumentParser(description="query PyMigBench")
    parser.add_argument("query", nargs='?', default="count",
                        choices=["count", "list", "detail", "c", "l", "d"],
                        help="The query you want to run")
    parser.add_argument("-d", "-dt", "--data-types", nargs='+',
                        help="The data types that you want to fetch. "
                             "Different queries accept different numbers of arguments.",
                        choices=["all", "lp", "mg", "cc"])
    parser.add_argument("-f", "--filters", required=False, nargs='+',
                        help="Additional filters. The format varies based on the query.")

    dict = vars(parser.parse_args())
    return Arguments(**dict)

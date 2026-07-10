from app.parsers.excel_parser import ExcelParser


def parse_excel(file_path: str):
    parser = ExcelParser(file_path)
    return parser.parse()
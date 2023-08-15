def parse_url(url):
    components = url.split("://")
    protocol = components[0]
    
    rest = components[1]
    domain_end = rest.find("/")
    domain = rest[:domain_end]
    
    path_start = domain_end
    path_end = rest.find("?")
    path = rest[path_start:path_end] if path_end != -1 else rest[path_start:]
    
    query_params = {}
    if path_end != -1:
        query_string = rest[path_end + 1:]
        query_pairs = query_string.split("&")
        for pair in query_pairs:
            key, value = pair.split("=")
            query_params[key] = value
    
    return {
        "protocol": protocol,
        "domain": domain,
        "path": path,
        "query_params": query_params
    }

def main():
    with open("input1.txt", "r") as input_file:
        url = input_file.readline().strip()

    parsed_url = parse_url(url)

    with open("output1.txt", "w", encoding="utf-8") as output_file:
        output_file.write("Протокол: {}\n".format(parsed_url["protocol"]))
        output_file.write("Домен: {}\n".format(parsed_url["domain"]))
        output_file.write("Путь: {}\n".format(parsed_url["path"]))
        output_file.write("Параметры запроса: {}\n".format(parsed_url["query_params"]))

if __name__ == "__main__":
    main()

print("Данные добавлены в output1.txt")

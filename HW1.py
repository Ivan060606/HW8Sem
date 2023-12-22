import os
import json
import csv
import pickle


def get_directory_size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total += os.path.getsize(filepath)
        return total

def directory_walker(path):
    results = []
    for root, dirs, files in os.walk(path):
        dirname = os.path.basename(root)
        dirsize = get_directory_size(root)
        results.append({'parent_directory': os.path.dirname(root), 
                        'type': 'directory',
                        "name": dirname,
                        "size_in_bytes": dirsize})

        for file in files:
            filepath = os.path.join(root, file)
            filesize = get_directory_size(filepath)
            results.append({"parent_directory": os.path.dirname(filepath), 
                            "type": 'file',
                            "name": file,
                            "size_in_bytes": filesize})
    return results

def save_results(path):
    results = directory_walker(path)
    with open("output.json", "w") as json_file:
        json.dump(results, json_file, indent=2, ensure_ascii=False)

    with open("output.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=results)
        writer.writeheader()
        writer.writerows(results)

    with open("output.pickle", "wb") as pickle_file:
        pickle.dump(results, pickle_file)



if __name__ == '__main__':
    save_results("C:\\Users\\Str\\Desctop\\python")
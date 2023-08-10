
def processing_list_from_file(file_path):
    list_id = []
    with open(file_path, 'r') as f: 
        lines = f.readlines()

    for line in lines:
        if line[:-1] != "":
            list_id.append(line[:-1])
    
    # validate unique
    list_id_set = set(list_id)
    unique_list_ids = (list(list_id_set))
    return unique_list_ids

def write_list_to_txt_file(file_path, list_arr):
    with open(file_path, 'w') as fp:
        for item in list_arr:
            fp.write("%s\n" % item)
    
def main():
    # error file
    error_ids_file = "log/error_ids.txt"
    object_ids_file = "object_id.txt"
    write_list_to_txt_file(error_ids_file, processing_list_from_file(error_ids_file))

    # object_id
    obj_ids =  processing_list_from_file(object_ids_file)
    error_ids = processing_list_from_file(error_ids_file)

    new_ids = set(obj_ids) - set(error_ids)
    write_list_to_txt_file(object_ids_file, new_ids)
main()
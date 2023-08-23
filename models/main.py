# (other imports)

if __name__ == '__main__':
    # ... (other code)

    num_farms = int(input("Enter number of farms: "))
    for i in range(1, num_farms + 1):
        size = input(f"Enter size of farm {i}: ")
        location = input(f"Enter location of farm {i}: ")
        crop_type = input(f"Enter crop type for farm {i}: ")
        crop_size = input(f"Enter crop size for farm {i}: ")
        user.add_farm(size=size, location=location, crop_type=crop_type, crop_size=crop_size)

    user_dict = user.to_dict()
    json_filename = 'user_data.json'
    with open(json_filename, 'w') as json_file:
        json.dump(user_dict, json_file)

    print(f"User data saved to '{json_filename}'.")

# ... (other imports)

class FarmConsole(cmd.Cmd):
    # ... (other methods and attributes)

    def do_add_farms(self, arg):
        """Add multiple farms to the user"""
        if not self.user:
            print("No user exists. Use 'create_user' command first.")
            return

        num_farms = int(arg)
        for i in range(1, num_farms + 1):
            size = input(f"Enter size of farm {i}: ")
            location = input(f"Enter location of farm {i}: ")
            crop_type = input(f"Enter crop type for farm {i}: ")
            crop_size = input(f"Enter crop size for farm {i}: ")
            self.user.add_farm(size=size, location=location, crop_type=crop_type, crop_size=crop_size)

        print(f"{num_farms} farms added successfully.")

    # ... (other methods)

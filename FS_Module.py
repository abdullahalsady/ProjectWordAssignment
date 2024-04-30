from fs import open_fs

def collect_user_data():
    print("Welcome! Please provide some information:")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email address: ")
    return f"Name: {name}, Age: {age}, Email: {email}"

def create_file_and_store_data(data):
    with open_fs('osfs://./') as fs:
        with fs.open('user_data.txt', 'w') as f:
            f.write(data)

def main():
    user_data = collect_user_data()
    create_file_and_store_data(user_data)
    print("Data has been successfully stored in user_data.txt")

if __name__ == "__main__":
    main()

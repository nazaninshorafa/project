import mysql.connector


class images:
    def __init__(self, id, title, tag, description, category):
        self.id = id
        self.title = title
        self.tag = tag
        self.description = description
        self.category = category

    def __str__(self):
        image = f"name:{self.title}, tag:{self.tag}"
        return image

class photographers:
    def __init__(self, photographer_code, photographer_name, photographer_email):
        self.photographer_code = photographer_code
        self.photographer_name = photographer_name
        self.photographer_email = photographer_email

    def __str__(self):
        photographer = f"name:{self.photographer_name}, email:{self.photographer_email}"
        return photographer

class articles:
    def __init__(self, id, keywords, title, category):
        self.id = id
        self.keywords = keywords
        self.title = title
        self.category = category
    
    def __str__(self):
        article = f"name:{self.keywords}, title:{self.title}"
        return article
    
class writers:
    def __init__(self, writer_code, writer_name, writer_email):
        self.writer_code = writer_code
        self.writer_name = writer_name
        self.writer_email = writer_email

    def __str__(self):
        writer = f"name:{self.writer_name}, email:{self.writer_email}"
        return writer

class DB:
    def __init__(self, user, password, host, datbase):
        self.user = user
        self.password = password
        self.host = host
        self.database = datbase
        self.connect = None

    def connection(self):
        self.connect = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host = self.host,
            database = self.database,
        )

    def execute_query(self, query, data=None, fetch=False):
        try:
            self.connect = self.connection()
            mycursor = self.connect.cursor()
            mycursor.execute(query, data)
        except Exception as e:
            print(e)
        else:
            if fetch:
                data = mycursor.fetchall()
                return data
            self.connect.commit()
            print("Done")
        finally:
            mycursor.close()
            self.connect.close()

    #Images
            
    def add_images(self, image):
        sql = "INSERT INTO images VALUES (%s, %s, %s, %s, %s)"
        data = (image.id_, image.title, image.tag, image.description, image.category)
        self.execute_query(sql, data)

    def remove_images(self, image_id):
        sql = "DELETE FROM images WHERE image_id=%s"
        data = (image_id)
        self.execute_query(sql, data)

    def list_images(self):
        category = input("Category: ")
        sql = "SELECT * FROM images"
        data = self.execute_query(sql, fetch=True)
        return data

    def update_images(self, image_id, title, tag, description, category):
        sql = f"UPDATE images SET {category}=%s WHERE category=%s"
        data = (category, image_id)
        self.execute_query(sql, data)

    #Articles    

    def add_articles(self, article):
        sql = "INSERT INTO articles VALUES (%s, %s, %s, %s)"
        data = (article.id_, article.keywords, article.title, article.category)
        self.execute_query(sql, data)

    def remove_articles(self, article_id):
        sql = "DELETE FROM images WHERE article_id=%s"
        data = (article_id)
        self.execute_query(sql, data)

    def list_articles(self):
        category = input("Category: ")
        sql = "SELECT * FROM articles"
        data = self.execute_query(sql, fetch=True)
        return data

    def update_articles(self, article_id, keywords, title, category):
        sql = f"UPDATE article SET {category}=%s WHERE category=%s"
        data = (category, article_id)
        self.execute_query(sql, data)
    
    #Photoghraphers

    def list_photographers(self):
        sql = "SELECT * FROM photographers"
        data = self.execute_query(sql, fetch=True)
        return data
    
    #Writers

    def list_writers(self):
        sql = "SELECT * FROM writers"
        data = self.execute_query(sql, fetch=True)
        return data


def main_menu():
    while True:
        print("\nImages and Articles Website")
        print("1. Add Image")
        print("2. Remove Image")
        print("3. Images List")
        print("4. Update Image")
        print("5. Add Article")
        print("6. Remove Article")
        print("7. Articles List")
        print("8. Update Article")
        print("9. Photographers List")
        print("10. Writers List")
        print("11. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_images()
        elif choice == '2':
            remove_images()
        elif choice == '3':
            list_images()
        elif choice == '4':
            update_images()
        elif choice == '5':
            add_articles()
        elif choice == '6':
            remove_articles()
        elif choice == '7':
            list_articles()
        elif choice == '8':
            update_articles()
        elif choice == '9':
            list_photoghraphers()
        elif choice == '10':
            list_writers()
        elif choice == '11':
            break
        else:
            print("Invalid! Please try again.")


if __name__ == "__main__":
    ai_website = DB("root","pass","localhost","DBblog")
    image = images(1000, "title", "tag", "description", "category")
    photographer = photographers(1000, "photographer_name", "photographer_email")
    article = articles(1000, "keyworks", "title", "category")
    writer = writers(1000, "writer_name", "writer_email")
    ai_website.add_images(image)
    ai_website.add_articles(article)
    print(ai_website.list_images())
    print(ai_website.list_photographers())
    print(ai_website.list_articles())
    print(ai_website.list_writers())
    ai_website.update_data(1000, "title1000", "tag", "description", "category")   
    ai_website.update_data(1000, "photographer_name", "photographer_email")   
    ai_website.update_data(1000, "keyworks", "title1000", "category")   
    ai_website.update_data(1000, "writer_name", "writer_email")   


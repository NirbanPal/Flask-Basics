This is just a page where we can keep track of employee. we can Add, Read, Edit and Remove the employees here.

**➤ Tech used :**
<p> HTML , CSS, BOOTSTRAP, JAVASCRIPT, FLASK, POSTGRESQL</p>

**➤ Setup this project :**

1. Clone this git repo->

    ```git
    git clone https://github.com/NirbanPal/ChatX.git
    ```

2. Go to the directory->

   ```shell
   cd ChatX
   ```
3. Create virtual environment->

   ```python
   python -m venv myenv
   ```
4. Activate virtual environment->

    For Windows->
  
   ```shell
   myenv\Scripts\activate
   ```
    For Linux->
  
   ```shell
   myenv/bin/activate
   ```

5. Install dependencies->
   
   ```python
   pip install -r requirements.txt
   ```
   
6. Create a database in postgresql and edit this line in application.py file->

   ```python
   app.config['SQLALCHEMY_DATABASE_URI']='postgresql://your_username:your_password@localhost/your_database_name'
   ```

7. Run the application->
   
   ```python
   python application.py
   ```

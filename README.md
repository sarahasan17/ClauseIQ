# Legal_Doc_Simplifier

## Setup Instructions

### Backend Setup

1. **Update the `.env` file:**  
   - Navigate to the `backend` folder.
   - Use the `.env.example` file as a reference to configure your API keys.

2. **Run the backend server:**
   ```sh
   uvicorn app.main:app --reload
   ```

3. **Test API Endpoints:**
   - Open your browser or use Postman to access:
     ```
     http://127.0.0.1:8000/docs
     ```
   - This will open the Swagger UI for API testing.

### Frontend Setup

1. **Install Angular CLI globally (if not installed):**
   ```sh
   npm install -g @angular/cli
   ```

2. **Navigate to the `frontend` folder** and install dependencies:
   ```sh
   npm install jquery
   npm install bootstrap
   npm install pdfjs-dist@latest
   npm install ngx-markdown
   ```

3. **Run the frontend application:**
   ```sh
   ng serve
   ```

4. **Access the frontend in your browser:**
   ```
   http://localhost:4200
   ```

### Additional Notes
- Ensure both the backend and frontend are running simultaneously for full functionality.
- Modify the `.env` file carefully to avoid exposing sensitive information.
- If you encounter errors, check logs in both backend and frontend terminals.


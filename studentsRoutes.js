// import express from "express";
// import {getstudents} from "../controllers/studentController.js"

// //router object
// const router=express.Router();


// router.get("/",getstudents());

// export default router


import express from "express";
import { getstudents,
    getStudentById,
    addStudent } from "../controllers/studentController.js";

const router = express.Router();
//get all the students
router.get("/", getstudents);  
//get student by id 
router.get("/:id",getStudentById)


//post  adding the student
router.post("/",addStudent)
//put updating the student
router.put("/id",updateStudent);

//delete the student by id 
router.delete("/delete",deleteStudent);


export default router;
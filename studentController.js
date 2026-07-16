let students=[
    {

        id:100,
        name:"rahje",
        phone:23133,
        branch:"cse",
        cgpa:0
    }
]


 export function getstudents(req,res){
    res.status(200).json(students)

};

 export function getStudentById(req,res){
    //read the id from the url
    const id =Number(req.params.id);
    //search the students 
    const student=students.find(
        (student)=>student.id===id
    );
    //if student s not found
    if (!student){
        return res.status(404).json({
            sucess:false,
            message:"student is not found"
        });
        };
    

    //return student:
    res.status(200).json({
        sucess:true,
        student

    });


}
//adding a student:
export function addStudent(req,res){
    //read the data--react form
    const student=req.body;
    //add inti the array
    student.push(student);
    res.status(201).json({
        sucess:true,
        message:"student registration sucessful",

        student
    })
}

export function updateStudent(req,res){
    const id=Number(req.params.id);
    const updateStudent=req.body;
    let studentFound=false;
    students=students.map((student)=>
    {
        if (students.id===id)
           {   
            studentaFound=true;
            }
        
    })
}


export function deleteStudent(req,res){
    const id=Number(req.params.id);
    const student=students.find(
        (student)=>student.id===id
    );
    student=student.filter(
        (student)=>student.id !== id
    );
    res.status(200).json({
    sucess:true,
    message:"student deleted sucessfully"

    })
}
import express, { Request, Response } from "express"

export const userRouter = express();

//GET endpoint for profiles
userRouter.get("/profiles", (req: Request, res: Response) => {
    res.json({
        msg : "Hello Profiles"
    })
})

//GET endpoints for jobs
userRouter.get("/jobs", (req: Request, res: Response) => {
    res.json({
        msg : "Hello Jobs"
    })
})
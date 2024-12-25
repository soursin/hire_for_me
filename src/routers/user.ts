import express, { Request, Response } from "express"
import { jobModel, profileModel } from "../models/schema";
import { z } from "zod";

export const userRouter = express();

interface Job{
    location?: string,
    skills?: { $in:string[]},
    description ?: {  $in:string[]},
    experience ?: number
}

userRouter.post("/jobs", async (req: Request, res: Response) => {
    const bodySchema = z.object({
        location : z.string().optional(),
        skills: z.array(z.string()).optional(),
        description: z.array(z.string()).optional(),
        experience : z.number().optional()
    })

    const validSchema = bodySchema.safeParse(req.body);
    if (!validSchema.success) {
        res.status(400).json({
            msg:"Invalid Body"
        })
    }

    try {

        let filter: Job = {};

        if (req.body.location) {
            filter.location = req.body.location;
        }

        if (req.body.skills && req.body.skills.length > 0) {
            filter.skills = { $in: req.body.skills };  
        }

        if (req.body.description && req.body.description.length > 0) {
            filter.description = { $in: req.body.description }; 
        }

        if (req.body.experience) {
            filter.experience = req.body.experience;
        }

        const jobs = await jobModel.find(filter);

        res.status(200).json({
            jobs: jobs
        })
        
    } catch (e) {
        res.status(500).json({
            msg:"Something Went Wrong"
        })
    }
    
})


userRouter.get("/profiles", (req: Request, res: Response) => {
    res.json({
        msg:"In progress"
    })
})



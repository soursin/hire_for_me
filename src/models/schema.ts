import mongoose, { Schema, model } from "mongoose";

const jobSchema = new Schema({
    job_id: { type: String, unique: true },
    link: { type: String, unique: true },
    company_name: { type: String },
    title : {type: String},
    location: { type: [String],default:[] },
    skills: { type: [String], default: [] },
    description: { type: [String], default: [] },
    experience : {type : Number, default : 0}
})

const profileSchema = new Schema({
    name: { type: String },
    skills: { type: [String] },
    education: { type: [String] },
    location: { type: [String] },
    title: { type: [String] },
    experience : {type : Number, default : 0}
})


export const jobModel = mongoose.model("jobs", jobSchema);
export const profileModel = mongoose.model("profiles", profileSchema);
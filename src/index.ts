import express,{Request , Response} from "express";
import { userRouter } from "./routers/user";
import mongoose from "mongoose";
import * as dotenv from "dotenv";

dotenv.config();
const app = express();

//middleware
app.use(express.json());
app.use("/user", userRouter);

async function main(port: number) {
    app.listen(port);
    await mongoose.connect(process.env.database as string);
    console.log(`Backend Running at port ${port} and Database connected`);
}

main(3000);
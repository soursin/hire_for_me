import express,{Request , Response} from "express";
import { userRouter } from "./routers/user";
const app = express();

//middleware
app.use("/user", userRouter);



app.listen(3000);
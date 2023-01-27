import "./index.css";
import axios from "axios";
import React from "react";
import { Button, Input, TextField } from "@mui/material";
import { Context } from "./SearchEngine";
import Images from "./Images";

function Header() {
  const [img, setImg] = React.useState(null);

  const [images, setImages] = React.useState([]);
  const [metaSearch, setMetaSearch] = React.useState("");
  const [imgToUpload, setImgToUpload] = React.useState(null);
  const [metaToUpload, setMetaToUpload] = React.useState("");

  const handleSubmit = React.useCallback(async () => {
    const formData = new FormData();
    if (!img) return;

    const res = await axios.post(
      "https://d32bdp38hd.execute-api.eu-central-1.amazonaws.com/images",
      img
    );

    const res2 = await axios.post("http://23.88.117.114/api/images/search", {
      url: res.data.url,
    });

    setImages(res2.data);
  }, [img]);

  const handleUpload = React.useCallback(async () => {
    const formData = new FormData();
    if (!imgToUpload) return;
    formData.append("image", imgToUpload);

    const res = await axios.post(
      "https://d32bdp38hd.execute-api.eu-central-1.amazonaws.com/images",
      imgToUpload
    );

    alert(metaToUpload);

    const res3 = await axios.post("http://23.88.117.114/api/images", {
      url: res.data.url,
      metadata: metaToUpload
    });

    // const res2 = await axios.post("http://23.88.117.114/api/images/search", {
    //   url: res.data.url,
    // });

    alert("Added successful");
  }, [imgToUpload, metaToUpload]);

  // @ts-ignore
  return (
    <div>
      <div
        style={{
          marginLeft: "100px",
          marginRight: "100px",
          borderLeft: "3px solid #581845",
        }}
      />
      <Input
        hidden
        type="file"
        // @ts-ignore
        onChange={(e) => setImgToUpload(e.target.files[0])}
      />
        <br/>

        <TextField
          style={{ marginTop: "20px" }}
          size="small"
          variant="outlined"
          label="Metedata (optional)"
          // @ts-ignore
          onChange={(e) => {setMetaToUpload(e.target.value);}}
        />


      <Button onClick={handleUpload} variant="contained" className="upload-btn">
        Upload
      </Button>
    </div>
  );
}

export default Header;

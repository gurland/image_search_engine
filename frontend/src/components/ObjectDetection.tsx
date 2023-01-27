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

  const [ss, setSS] = React.useState(null);

  const handleSubmit = React.useCallback(async () => {
    const formData = new FormData();
    if (!img) return;

    const res = await axios.post(
      "https://d32bdp38hd.execute-api.eu-central-1.amazonaws.com/images",
      img
    );

    const res2 = await axios.post(
      "http://23.88.117.114/api/images/object_detection",
      {
        url: res.data.url,
      },
      { responseType: "blob" }
    );

    console.log(res2);

    setSS(res2.data);

    // setImages(res2.data);
  }, [img]);

  const handleUpload = React.useCallback(async () => {
    const formData = new FormData();
    if (!imgToUpload) return;
    formData.append("image", imgToUpload);

    const res = await axios.post(
      "https://d32bdp38hd.execute-api.eu-central-1.amazonaws.com/images",
      imgToUpload
    );

    const res3 = await axios.post(
      "http://23.88.117.114/api/images/object_detection",
      {
        url: res.data.url,
      }
    );

    alert("Added successful");
  }, [imgToUpload]);

  return (
    <div className="header-wrapper">
      <div className="wrap-wrap">
        <Input
          hidden
          type="file"
          // @ts-ignore
          onChange={(e) => setImg(e.target.files[0])}
        />

        <Button
          onClick={handleSubmit}
          variant="contained"
          className="upload-btn"
        >
          Search
        </Button>
      </div>

      {ss && (
        <img
          style={{ marginTop: "40px", maxWidth: "600px", maxHeight: "600px" }}
          src={URL.createObjectURL(ss)}
        />
      )}
      {/* <Images images={images} /> */}

      {/* <TextField
          style={{ marginTop: "20px" }}
          size="small"
          variant="outlined"
          label="Metedata search"
          onChange={(e) => setMetaSearch(e.target.value)}
        /> */}
      {/* <div
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

      <Button onClick={handleUpload} variant="contained" className="upload-btn">
        Upload
      </Button> */}
    </div>
  );
}

export default Header;

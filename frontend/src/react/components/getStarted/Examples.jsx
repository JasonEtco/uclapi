import React from 'react';
import {
  Card,
  CardActions,
  CardHeader,
  CardMedia,
  CardTitle,
  CardText
} from 'material-ui/Card';
import FlatButton from 'material-ui/FlatButton';


const Example = (title, imageLink, description, link, key) => (
  <Card className="example" zDepth={2} key={key}>
    <CardMedia>
      <img src={imageLink}/>
    </CardMedia>
    <CardTitle title={title}/>
    <CardText>
      {description}
    </CardText>
    <CardActions>
      <a href={link}>
        <FlatButton label="View"/>
      </a>
    </CardActions>
  </Card>
)


let examples = [
  {
    title: "Veruto",
    imageLink: "https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png",
    description: "A mobile app that finds the closest free room in UCL",
    link: "https://github.com/uclapi/veruto"
  }, {
    title: "Society Visualisation",
    imageLink: "https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png",
    description: "A calendar visualisation of Society Room Bookings at UCL",
    link: "https://github.com/uclapi/society-visualisation"
  }, {
    title: "RB Calendar",
    imageLink: "https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png",
    description: "Turn UCL API room bookings into ics calendar events.",
    link: "http://rbcalendar.uclapi.com"
  }, {
    title: "UCLKit",
    imageLink: "https://maxcdn.icons8.com/Share/icon/color/Programming//swift1600.png",
    description: "UCL API wrapper in Swift",
    link: "https://github.com/tiferrei/UCLKit"
  }, {
    title: "uclapi-go",
    imageLink: "http://www.unixstickers.com/image/data/stickers/golang/Go-aviator.sh.png",
    description: "A wrapper library in Go for uclapi",
    link: "https://github.com/Maaarcocr/uclapi-go"
  }, {
    title: "uclapi-javascript",
    imageLink: "https://avatars0.githubusercontent.com/u/6078720?v=3&s=400",
    description: "JavaScript wrapper for the UCL API. Works both in the browser and in Node.",
    link: "https://github.com/HugoDF/uclapi-javascript"
  }
]


export default class Examples extends React.Component {

  render() {
    return (
      <div className="container pad">
        <h1 className="center">Built Using UCL API</h1>
        <div className="examples">
          {examples.map((eg, i) => Example(eg.title, eg.imageLink, eg.description, eg.link, i))}
        </div>
      </div>
    )
  }

}

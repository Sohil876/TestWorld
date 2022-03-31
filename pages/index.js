import Head from 'next/head'
import styles from '../styles/Home.module.css'
import SkillsCards from './cards/skills.js'

/*
import Image from 'next/image'
// opt-out of image optimization, no-op
const customLoader = ({ src }) => {
  return src
}
*/

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>MySite</title>
        <meta name="description" content="Test site built with next.js" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>

        <div className={styles.description}>
          <h1> Halo <a href="#"> Warld! </a></h1>
          Hi, i am &nbsp;
          <code className={styles.code}>Arsh Khan</code>
        </div>

        <div className={styles.splashBgParent}>
          <video className={styles.splashBg} poster="splash-poster.webp" autoPlay muted loop>
            <source src="splash-bg.webm" type="video/webm" />
          </video>
          
          <img alt="Sohil876" className={styles.profilePic}
            src="profPic.png" />
        </div>

        <h2>My Skills:</h2>
        <div className={styles.grid}>
          <SkillsCards />
        </div>

      </main>

      <footer className={styles.footer}>
        <span className={styles.footerCard}>
          © 2018-2022 &nbsp;
          <a href="https://github.com/Sohil876"
            target="_blank" rel="noreferrer">
            Arsh Khan
          </a>
        </span>
      </footer>
    </div>
  )
}


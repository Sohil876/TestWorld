import styles from '../../styles/SkillsCards.module.css'

export default function SkillsCards() {
  return(
    <>
      <div className={styles.card}>
        <p className={styles.listTitle}>HTML</p>
        <ul>
          <li>HTML4.x <b className={styles.done}>(Done)</b></li>
          <li>HTML5.x <b className={styles.todo}>(ToDo)</b></li>
        </ul>
      </div>
    
      <div className={styles.card}>
        <p className={styles.listTitle}>CSS</p>
        <ul>
          <li>CSS <b className={styles.done}>(Done)</b></li>
          <li>CSS3 <b className={styles.todo}>(ToDo)</b></li>
        </ul>
      </div>

      <div className={styles.card}>
        <p className={styles.listTitle}>JavaScript</p>
        <ul>
          <li>JS <b className={styles.done}>(Done)</b></li>
          <li>JS6 <b className={styles.done}>(Done)</b></li>
          <li>JSX <b className={styles.done}>(Done)</b></li>
          <li>React <b className={styles.learning}>(Learning)</b></li>
          <li>React-Native <b className={styles.learning}>(Learning)</b></li>
          <li>NextJS <b className={styles.learning}>(Learning)</b></li>
          <li>NodeJS <b className={styles.done}>(Done)</b></li>
          <li>SystemJS <b className={styles.maybetodo}>(Maybe ToDo)</b></li>
          <li>JQuery <b className={styles.maybetodo}>(Maybe ToDo)</b></li>
        </ul>
      </div>

      <div className={styles.card}>
        <p className={styles.listTitle}>Python</p>
        <ul>
          <li>Python 3.x <b className={styles.done}>(Done)</b></li>
          <li>Kivy <b className={styles.done}>(Done)</b></li>
          <li>Django <b className={styles.todo}>(Maybe ToDo)</b></li>
        </ul>
      </div>

      <div className={styles.card}>
        <p className={styles.listTitle}>Lua</p>
        <ul>
          <li>Lua 5.x <b className={styles.done}>(Done)</b></li>
          <li>LOVE2D <b className={styles.done}>(Done)</b></li>
        </ul>
      </div>

      <div className={styles.card}>
        <p className={styles.listTitle}>Terminal</p>
        <ul>
          <li>Bash <b className={styles.done}>(Done)</b></li>
          <li>ZSH <b className={styles.done}>(Done)</b></li>
          <li>Git <b className={styles.done}>(Done)</b></li>
        </ul>
      </div>
    </>
  )
}
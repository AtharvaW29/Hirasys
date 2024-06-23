import Image from 'next/image'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUser } from '@fortawesome/free-regular-svg-icons'
import { SideBarItem, SideBarNavDrawer } from './SideBarItems'

const SideBar = () => {
  return (
    <div className="h-screen w-[20%] sticky top-0 left-0 py-3 px-4 bg-overlay border-r-1 space-y-10">
      <Image
        src={'/images/mainLogo.png'}
        alt="Hirasys Logo"
        width={180}
        height={200}
      />
      <div className="space-y-3 ">
        <SideBarNavDrawer />
        <SideBarItem
          isActive
          name={`Accounts`}
          icon={<FontAwesomeIcon icon={faUser} className="w-[1rem] h-[1rem]" />}
        />
      </div>
    </div>
  )
}

export default SideBar
